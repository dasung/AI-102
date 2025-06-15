1] To get list of Keys:
    `az cognitiveservices account keys list --name my-ai-service-0523 --resource-group my-res-group-0523`
    {
        "key1": "80JQQJ99BEACYeBjFXJ3w3AAAEACOGSJPb",
        "key2": "82JQQJ99BEACYeBjFXJ3w3AAAEACOGvEtm"
    }
2] To create service principal (acess key valt)
`az ad sp create-for-rbac -n "api://my-ai-app" --role owner --scopes subscriptions/a17493b3-c6f4-43b8-aab4-7dad5e11118d/resourceGroups/my-res-group-0523`
    {
    "appId": "a2d37a71-7f43-4507-9606-b0cfc56d1b89",            # This is your client_id
    "displayName": "api://my-ai-app",
    "password": "yyc8Q~jiC.BXwIJAVONT-gvy6bpHX~XfHb~CjaKX",     # This is your client_secret
    "tenant": "40b9bc57-e3eb-4d3b-80db-ad123ac9a09a"            # This is your tenant_id
    }

    * To get <object id> of this [service principle]
        az ad sp show --id <appId>
        (<object id> is the "id" value in the json returned in response)

    * To assign permission for your [service principal] to access secrets in your Key Vault.
        az keyvault set-policy -n my-key-vault-0523 --object-id <object id> --secret-permissions get list
    