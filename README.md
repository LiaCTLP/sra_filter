# sra_filter
For marketing search


Search companies with additional filters for location and practice area

examle: 
http://127.0.0.1:5000/filtered_companies?location=london&practice_area=litigation


{
        "AuthorisationDate": "2015-11-01T00:00:00",
        "AuthorisationStatus": "YES",
        "AuthorisationStatusDate": "2015-11-01T00:00:00",
        "AuthorisationType": "RECSOLE",
        "CompanyRegNo": null,
        "Constitution": "SOLP",
        "FreelanceBasis": null,
        "Id": 209268,
        "NoOfOffices": 1,
        "Offices": [
            {
                "Address1": "56 Queensway",
                "Address2": null,
                "Address3": null,
                "Address4": null,
                "Country": "England",
                "County": null,
                "Email": "jbcalver@yahoo.co.uk",
                "Name": "JOHN B CALVER & CO",
                "OfficeId": 44618,
                "OfficeType": "HO",
                "PhoneNumber": "02072219181",
                "Postcode": "W2 3RY",
                "Town": "LONDON",
                "Website": null
            }
        ],
        "OrganisationType": "FIRMSRA",
        "PracticeName": "JOHN B CALVER & CO",
        "PreviousNames": null,
        "Regulator": "SRA",
        "ReservedActivites": null,
        "SraNumber": 44618,
        "TradingNames": null,
        "Type": "RecognisedSolePracticeAuthorised",
        "Websites": null,
        "WorkArea": [
            "Property - Residential",
            "Non-Litigation - Other",
            "Property - Commercial",
            "Probate and Estate Administration"
        ]
    }




Example of practice areas : 

VALID_PRACTICE_AREAS = [
    "administrative law", "banking law", "commercial law", "corporate law",
    "criminal law", "employment law", "environmental law", "family law",
    "human rights law", "immigration law", "intellectual property law",
    "personal injury law", "property law", "tax law", "wills and probate","Landlord and Tenant","Employment","Litigation"
]


However, It can just search any and it will show matches. Most records does not show the work area/ practice area


to get all companyies just search /filtered_companies
