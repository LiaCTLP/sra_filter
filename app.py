from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SRA_API_URL = "https://sra-prod-apim.azure-api.net/datashare/api/V1/organisation/GetAll"
API_KEY = "37f57afeafcd4630bd698188c848fa1b"

VALID_PRACTICE_AREAS = [
    "administrative law", "banking law", "commercial law", "corporate law",
    "criminal law", "employment law", "environmental law", "family law",
    "human rights law", "immigration law", "intellectual property law",
    "personal injury law", "property law", "tax law", "wills and probate","Landlord and Tenant","Employment","Litigation"
]


# API Key and Authentication
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

    location = request.args.get('location', '').strip().lower()
    practice_area = request.args.get('practice_area', '').strip().lower()


    companies = fetch_sra_companies()
    print(f"Fetched Companies: {len(companies)} companies found.")


    if not companies:
        return jsonify({"error": "No companies found or API request failed"}), 404

    filtered_companies = []

    for company in companies:
        office_matches = False
        work_area_matches = False

        print(f"Company Details: {company}")


        if company.get('Offices'):
            for office in company['Offices']:
                print(f"Office: {office}")
                if location and (
                        location in (office.get('Town') or '').lower() or
                        location in (office.get('County') or '').lower() or
                        location in (office.get('Postcode') or '').lower()
                ):
                    office_matches = True
                    break


        if company.get('WorkArea'):
            print(f"WorkArea: {company.get('WorkArea')}")
            work_area_matches = any(practice_area in area.lower() for area in company['WorkArea'])


        if (not location or office_matches) and (not practice_area or work_area_matches):
            filtered_companies.append(company)

    print(f"Filtered Companies: {len(filtered_companies)}")
    return jsonify(filtered_companies)


if __name__ == '__main__':
    app.run(debug=True)
