from config import config

def check_fields(args):
    arg_keys = args.keys()
    missing_fields = list(filter(lambda required_field: required_field not in arg_keys, config["REQUIRED_FIELDS"]))
    
    return {"status": False,"message": "Missing fields: {}".format(", ".join(missing_fields))} \
        if len(missing_fields) \
            else {"status": True}

def validation(args):
   return check_fields(args)
