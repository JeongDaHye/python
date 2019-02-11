from faker import Faker

#Faker의 메소드를 통해 어떤 종류의 가짜 데이터를 뽑아낼 것인지 결정하는 기능  
myfake = Faker()
myfake.seed(1)
print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.state())
print(myfake.sentence())
print(myfake.random_number())

#한국어 
ko_fake = Faker('ko_KR')
ko_fake.seed(2)
print('')
print(ko_fake.name())
print(ko_fake.address())
print(ko_fake.random_number())