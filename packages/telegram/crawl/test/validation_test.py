from ..config import config
from ..crawl import main
import unittest

class ValidationTest(unittest.TestCase):
  
    def test_missing_required_keys(self):
        args = {
          "name": "test_name"
        }
        response = main(args)
        arg_keys = args.keys()
        missing_fields = list(filter(lambda required_field: required_field not in arg_keys, config["REQUIRED_FIELDS"]))

        self.assertEqual(response["message"], "Missing fields: {}".format(", ".join(missing_fields)))

if __name__ == '__main__':
  unittest.main()