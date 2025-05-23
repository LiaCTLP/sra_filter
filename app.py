from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from fuzzywuzzy import fuzz, process

app = Flask(__name__)
CORS(app)

SRA_API_URL = "https://sra-prod-apim.azure-api.net/datashare/api/V1/organisation/GetAll"
API_KEY = "37f57afeafcd4630bd698188c848fa1b"

VALID_PRACTICE_AREAS = ["Administrative ", "Banking ", "Commercial ", "Corporate ",
                        "Criminal ", "Employment ", "Environmental ", "Family ",
                        "Human Rights ", "Immigration ", "Intellectual Property ",
                        "Personal Injury ", "Property ", "Tax ", "Wills and Probate", "Landlord and Tenant",
                        "Employment", "Litigation"]


Keys_db = {
    '745cd00c-03ad-4LIA-a2f0-38ef6ca314ca': 'user1',
    'c5e5b22d-4773-4LIA-83ce-0011943f58b0': 'user2'
}


def fetch_sra_companies():
    headers = {"Ocp-Apim-Subscription-Key": API_KEY}
    response = requests.get(SRA_API_URL, headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        return response.json().get('Organisations', [])
    else:
        return []


def authenticate_api_key(api_key):
    return Keys_db.get(api_key)


@app.before_request
def before_request():
    api_key = request.headers.get('API-Key')
    if not api_key or not authenticate_api_key(api_key):
        return jsonify({'error': 'Unauthorized'}), 401


@app.route('/filtered_companies', methods=['GET'])
def get_filtered_companies():

    practice_name = request.args.get('practice_name', '').strip().lower()
    location = request.args.get('location', '').strip().lower()
    practice_area = request.args.get('practice_area', '').strip().lower()

    print(f"Query Parameters - practice_name: {practice_name}, location: {location}, practice_area: {practice_area}")

    companies = fetch_sra_companies()
    print(f"Fetched Companies: {len(companies)} companies found.")

    if not companies:
        return jsonify({"error": "No companies found or API request failed"}), 404

    filtered_companies = []


    for company in companies:
        office_matches = False
        work_area_matches = False
        practice_name_matches = False

        # Log the company being processed
        print(f"Processing Company: {company}")


        if company.get('PracticeName'):
            print(f"Checking PracticeName: {company['PracticeName']}")
            if practice_name:
                match_score = fuzz.partial_ratio(practice_name, company['PracticeName'].lower())
                if match_score >= 95:
                    practice_name_matches = True
                    print(f"PracticeName matches: {company['PracticeName']} with score {match_score}")


        if company.get('Offices'):
            for office in company['Offices']:
                if location and (
                        location in (office.get('Town') or '').lower() or
                        location in (office.get('County') or '').lower() or
                        location in (office.get('Postcode') or '').lower()
                ):
                    office_matches = True
                    break


        if company.get('WorkArea'):
            work_area_matches = any(practice_area in area.lower() for area in company['WorkArea'])


        if (not location or office_matches) and (not practice_area or work_area_matches) and (
                not practice_name or practice_name_matches):
            filtered_companies.append(company)
        else:
            print(f"No match for company: {company.get('PracticeName', 'Unknown')}")

    print(f"Filtered Companies: {len(filtered_companies)}")


    return jsonify({
        "count": len(filtered_companies),
        "companies": filtered_companies
    })


if __name__ == '__main__':
    app.run(debug=True)
