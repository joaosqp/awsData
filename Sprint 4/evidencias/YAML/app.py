import yaml

teste = 'C:\Users\joao_\Desktop\Compass UOL\awsData\Sprint 4\evidencias\YAML\test.yamlc'

if __name__ == '__main__':

  stream = open(teste , "r")
  dictionary = yaml.safe_load(stream)

  for key, value in dictionary.items():
    print(key + " : " + str(value))