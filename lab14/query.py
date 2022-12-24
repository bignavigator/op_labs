from config import DATABASE_URI
from model import Lessons, Disciplines, DaysOfWeek, association_table, association_table2
from crud import get_session_engine
from sqlalchemy.orm import joinedload
import matplotlib.pyplot as plt

s, _ = get_session_engine(DATABASE_URI)

qry = s.query(Lessons, Disciplines, DaysOfWeek).options(joinedload(Lessons.numbers, innerjoin=False).\
        joinedload(Disciplines.lessons, innerjoin=True)).filter(Disciplines.id > Lessons.number-2).\
        filter(Disciplines.id < DaysOfWeek.id).filter(Disciplines.id > DaysOfWeek.id-2)

print(qry.statement)
query_res = qry.all()
query_dict = {}

pon_count = 0
vtor_count = 0
sre_count = 0
che_count = 0
piat_count = 0
sub_count = 0
for q in query_res:
    if q.Disciplines.name and q.DaysOfWeek.name != None:
        print(f'\t{q.Disciplines.name}, {q.DaysOfWeek.name}, пара номер: {q.Lessons.number}')
        match q.DaysOfWeek.name:
            case "ponedeljnik":
                pon_count += 1
            case "vtornik":
                vtor_count += 1
            case "sreda":
                sre_count += 1
            case "chetverg":
                che_count += 1
            case "piatnica":
                piat_count += 1
            case "subbota":
                sub_count += 1
print(f'\tПонедельник, число пар в этот день: {pon_count}')
print(f'\tВторник, число пар в этот день: {vtor_count}')
print(f'\tСреда, число пар в этот день: {sre_count}')
print(f'\tЧетверг, число пар в этот день: {che_count}')
print(f'\tПятница, число пар в этот день: {piat_count}')
print(f'\tСуббота, число пар в этот день: {sub_count}')

plt.bar(query_dict.keys(), [len(c) for c in query_dict.values()])
plt.show()
