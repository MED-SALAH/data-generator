from omegaconf import OmegaConf
import pandas as pd
from services.generator import Generator

def test_one_department_one_region():
    #given
    print("test begin .....")
    inputConf = OmegaConf.create(
                                    {
                                      "name": "sales",
                                      "format": "csv",
                                      "rows": 1,
                                      "columns": [
                                        {
                                          "name": "region",
                                          "dtype": "String",
                                          "choice": [
                                            "FR-IDF"
                                          ]
                                        },
                                        {
                                          "name": "departement",
                                          "dtype": "String",
                                          "dict": {
                                            "FR-IDF": [
                                              "Paris"
                                            ]
                                          }
                                        }
                                      ]
                                    })
    d = {'region': ['FR-IDF'], 'departement': ['Paris']}
    expected = pd.DataFrame(d)
    expected.
    print(expected)
    #when
    gn = Generator()
    df = gn.get_dataframe_from_dc(inputConf)
    print(df)
    #then
    assert True
