# This for check the results of scrapping...
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)
db = client['scrapyDB']

# Let's print 10 results from the both collections

for vacancy in db['superjob.ru'].find({})[:10]:
    pprint(vacancy)

for vacancy in db['hh.ru'].find({})[:10]:
    pprint(vacancy)

# Output example


# Connected to pydev debugger (build 192.7142.56)

# {'_id': ObjectId('5e059572fb21f45d6a0e7498'),
#  'link': 'https://www.superjob.ru/vakansii/web-razrabotchik-react-32675674.html',
#  'salary_from': '',
#  'salary_to': '',
#  'source': 'superjob.ru',
#  'title': 'Web-разработчик React',
#  'units': ''}
# {'_id': ObjectId('5e059572fb21f45d6a0e7499'),
#  'link': 'https://www.superjob.ru/vakansii/analitik-33308640.html',
#  'salary_from': 100000,
#  'salary_to': '',
#  'source': 'superjob.ru',
#  'title': 'Аналитик (отчетность)',
#  'units': '₽'}
# {'_id': ObjectId('5e059572fb21f45d6a0e749a'),
#  'link': 'https://www.superjob.ru/vakansii/specialist-po-avtomatizacii-biznes-processov-32970670.html',
#  'salary_from': '',
#  'salary_to': '',
#  'source': 'superjob.ru',
#  'title': 'Специалист по автоматизации бизнес-процессов',
#  'units': ''}
# {'_id': ObjectId('5e059572fb21f45d6a0e749b'),
#  'link': 'https://www.superjob.ru/vakansii/veduschij-sistemnyj-administrator-32969986.html',
#  'salary_from': '',
#  'salary_to': '',
#  'source': 'superjob.ru',
#  'title': 'Ведущий системный администратор',
#  'units': ''}
# {'_id': ObjectId('5e059572fb21f45d6a0e749c'),
#  'link': 'https://www.superjob.ru/vakansii/veduschij-sistemnyj-administrator-linux-33271316.html',
#  'salary_from': '',
#  'salary_to': '',
#  'source': 'superjob.ru',
#  'title': 'Ведущий системный администратор Linux',
#  'units': ''}
# {'_id': ObjectId('5e059572fb21f45d6a0e749d'),
#  'link': 'https://www.superjob.ru/vakansii/middle-33308712.html',
#  'salary_from': 200000,
#  'salary_to': '',
#  'source': 'superjob.ru',
#  'title': 'Middle / Senior Data Scientist',
#  'units': '₽'}
# {'_id': ObjectId('5e059572fb21f45d6a0e749e'),
#  'link': 'https://www.superjob.ru/vakansii/pomoschnik-sistemnogo-administratora-33278859.html',
#  'salary_from': 25000,
#  'salary_to': 31000,
#  'source': 'superjob.ru',
#  'title': 'Помощник системного администратора',
#  'units': '₽'}
# {'_id': ObjectId('5e059573fb21f45d6a0e749f'),
#  'link': 'https://www.superjob.ru/vakansii/programmist-python-32671953.html',
#  'salary_from': 50000,
#  'salary_to': '',
#  'source': 'superjob.ru',
#  'title': 'Программист Python (удалённо)',
#  'units': '₽'}
# {'_id': ObjectId('5e059573fb21f45d6a0e74a0'),
#  'link': 'https://www.superjob.ru/vakansii/veduschij-inzhener-programmist-32057893.html',
#  'salary_from': '',
#  'salary_to': '',
#  'source': 'superjob.ru',
#  'title': 'Ведущий инженер-программист',
#  'units': ''}
# {'_id': ObjectId('5e059573fb21f45d6a0e74a1'),
#  'link': 'https://www.superjob.ru/vakansii/inzhener-programmist-33274451.html',
#  'salary_from': 120000,
#  'salary_to': 150000,
#  'source': 'superjob.ru',
#  'title': 'Инженер-программист (Python)',
#  'units': '₽'}
# {'_id': ObjectId('5e05948632818582e7e4262d'),
#  'link': 'https://hh.ru/vacancy/34831620?query=python',
#  'salary_from': 200000,
#  'salary_to': 300000,
#  'source': 'hh.ru',
#  'title': 'Python Web Developer',
#  'units': 'руб. на руки'}
# {'_id': ObjectId('5e05949032818582e7e4262e'),
#  'link': 'https://hh.ru/vacancy/35124343?query=python',
#  'salary_from': 210000,
#  'salary_to': 280000,
#  'source': 'hh.ru',
#  'title': 'Python Fullstack',
#  'units': 'руб. на руки'}
# {'_id': ObjectId('5e05949332818582e7e4262f'),
#  'link': 'https://hh.ru/vacancy/35020789?query=python',
#  'salary_from': 80000,
#  'salary_to': 140000,
#  'source': 'hh.ru',
#  'title': 'Python-разработчик',
#  'units': 'руб. на руки'}
# {'_id': ObjectId('5e05949332818582e7e42630'),
#  'link': 'https://hh.ru/vacancy/33416348?query=python',
#  'salary_from': '',
#  'salary_to': 400000,
#  'source': 'hh.ru',
#  'title': 'Python разработчик / Python software developer',
#  'units': 'руб. на руки'}
# {'_id': ObjectId('5e05949432818582e7e42631'),
#  'link': 'https://hh.ru/vacancy/34890038?query=python',
#  'salary_from': 80000,
#  'salary_to': 120000,
#  'source': 'hh.ru',
#  'title': 'Backend разработчик Python / Django (Middle)',
#  'units': 'руб. на руки'}
# {'_id': ObjectId('5e0594a932818582e7e42632'),
#  'link': 'https://hh.ru/vacancy/35105576?query=python',
#  'salary_from': 150000,
#  'salary_to': 150000,
#  'source': 'hh.ru',
#  'title': 'Системный администратор Linux / DevOps',
#  'units': 'руб. на руки'}
# {'_id': ObjectId('5e0594ab32818582e7e42633'),
#  'link': 'https://hh.ru/vacancy/31954853?query=python',
#  'salary_from': '',
#  'salary_to': '',
#  'source': 'hh.ru',
#  'title': 'Data Engineer / ETL Developer',
#  'units': ''}
# {'_id': ObjectId('5e0594ac32818582e7e42634'),
#  'link': 'https://hh.ru/vacancy/33277482?query=python',
#  'salary_from': '',
#  'salary_to': '',
#  'source': 'hh.ru',
#  'title': 'Python-разработчик',
#  'units': ''}
# {'_id': ObjectId('5e0594ad32818582e7e42635'),
#  'link': 'https://hh.ru/vacancy/35097382?query=python',
#  'salary_from': 180000,
#  'salary_to': '',
#  'source': 'hh.ru',
#  'title': 'Backend Developer (Python, PostgreSQL)',
#  'units': 'руб. на руки'}
# {'_id': ObjectId('5e0594ae32818582e7e42636'),
#  'link': 'https://hh.ru/vacancy/33774758?query=python',
#  'salary_from': '',
#  'salary_to': '',
#  'source': 'hh.ru',
#  'title': 'Junior data engineer (внедрение моделей)',
#  'units': ''}
#
# Process finished with exit code 0
