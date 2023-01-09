from flat import Bill, Flatmates
from reports import PdfReport

amount = float(input('Input bill amount: '))
period = input('Bill period , Decemenber 2020: ')

name1 = input('what is your name?  ')
days_in_house1 = int(input(f'How many days {name1} was in house for period {period} '))

name2 = input('what is your flatmate name?  ')
days_in_house2 = int(input(f'How many days {name2} was in house for period {period} '))

bill = Bill(amount, period)
flatmate1 = Flatmates(name1, days_in_house1)
flatmate2 = Flatmates(name2, days_in_house2)

print(f"{flatmate1.name} pays:", flatmate1.pays(bill, flatmate2))
print(f"{flatmate2.name} pays:", flatmate2.pays(bill, flatmate1))

pdf_report = PdfReport(name=f'{bill.period}.pdf')
pdf_report.generate(flatmate1, flatmate2, bill)
