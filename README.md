# sra_filter
For marketing search


Search companies with additional filters for location and practice area

examle: 
http://127.0.0.1:5000/filtered_companies?practice_name=Riverine Solicitors&location=london&practice_area=family


{
  "companies": [
    {
      "AuthorisationDate": "2023-12-18T00:00:00",
      "AuthorisationStatus": "YES",
      "AuthorisationStatusDate": "2023-12-18T00:00:00",
      "AuthorisationType": "RECSOLE",
      "CompanyRegNo": null,
      "Constitution": "SOLP",
      "FreelanceBasis": null,
      "Id": 841308,
      "NoOfOffices": 1,
      "Offices": [
        {
          "Address1": "2-4 Commercial Street",
          "Address2": "ROOM 221",
          "Address3": "SECOND FLOOR",
          "Address4": null,
          "Country": "England",
          "County": null,
          "Email": "info@riverinesolicitors.co.uk",
          "Name": "Riverine Solicitors",
          "OfficeId": 8005864,
          "OfficeType": "HO",
          "PhoneNumber": "02086171210",
          "Postcode": "E1 6LP",
          "Town": "London",
          "Website": null
        }
      ],
      "OrganisationType": "FIRMSRA",
      "PracticeName": "Riverine Solicitors",
      "PreviousNames": null,
      "Regulator": "SRA",
      "ReservedActivites": null,
      "SraNumber": 8005864,
      "TradingNames": null,
      "Type": "RecognisedSolePracticeAuthorised",
      "Websites": null,
      "WorkArea": [
        "Family / Matrimonial",
        "Immigration",
        "Litigation - Other"
      ]
    }
  ],
  "count": 1
}



Example of practice areas : 

VALID_PRACTICE_AREAS = ["Administrative ", "Banking ", "Commercial ", "Corporate ",
                        "Criminal ", "Employment ", "Environmental ", "Family ",
                        "Human Rights ", "Immigration ", "Intellectual Property ",
                        "Personal Injury ", "Property ", "Tax ", "Wills and Probate", "Landlord and Tenant",
                        "Employment", "Litigation"]


However, It can just search any and it will show matches. Most records does not show the work area/ practice area


to get all companyies just search /filtered_companies
