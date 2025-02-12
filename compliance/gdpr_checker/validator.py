# compliance/gdpr_checker/validator.py
def validate_gdpr_compliance(data):
    return {
        "data_minimization": check_data_retention(data),
        "right_to_be_forgotten": check_deletion_paths(data)
    }