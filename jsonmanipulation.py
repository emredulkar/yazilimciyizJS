off = {
  "offers": [
    {
      "offerId": 1,
      "contractId": "1",
      "offerName": "Offer1",
      "contractName": "Contract1"
    },
    {
      "offerId": 2,
      "contractId": "1",
      "offerName": "Offer2",
      "contractName": "Contract1"
    },
    {
      "offerId": 3,
      "contractId": "2",
      "offerName": "Offer3",
      "contractName": "Contract2"
    }
  ]
}


allcontractid = []
for i in range(3):
    b =off["offers"][i]["contractId"]
    allcontractid.append(b)
print(allcontractid)

def unique_list(l):
    uniqcontractId = []
    for a in l:
        if a not in uniqcontractId:
            uniqcontractId.append(a)
    return uniqcontractId
uniqcontractId = unique_list(allcontractid)
print(uniqcontractId )


const_new = {"contracts": []}

conts = {
        "contractId" : " ",
        "contractName" :" ",
        "offers" : [
            {
            "offerId": "",
            "offerName": ""
            }
        ]
    }

for z in range(len(uniqcontractId)):
    m=0
    conts = {
        "contractId" : " ",
        "contractName" :" ",
        "offers" : [
            {
            "offerId": "",
            "offerName": ""
            }
        ]
    }
    
    for i in range(len(off["offers"])):
        
        if off["offers"][i]["contractId"] == uniqcontractId[z]:

            
            m=m+1
            if m >1 :
                const_new["contracts"][z]["offers"].append(
                    {"offerId": off["offers"][i]["offerId"],"offerName":off["offers"][i]["offerName"]})
               
            else:
                conts["offers"][0]["offerId"] = off["offers"][i]["offerId"]
                conts["offers"][0]["offerName"] = off["offers"][i]["offerName"]
                conts["contractId"]= off["offers"][i]["contractId"]
                conts["contractName"]= off["offers"][i]["contractName"]  
              
                const_new["contracts"].append(conts)    

print(const_new)
