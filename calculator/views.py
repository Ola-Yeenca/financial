from django.shortcuts import render
from .calculations import compound_interest, loan_payment, investment_return, present_value_input, future_value
from .forms import PersonalFinanceForm

def index(request):
    form = PersonalFinanceForm()
    return render(request, 'calculator/index.html', {'form': form})

def personal_finance_cal(request):
    if request.method == 'POST':
        form = PersonalFinanceForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            principal = data['principal']
            rate = data['rate']
            time = data['time']
            choice = data['choice']

            if choice == '1':
                result = compound_interest(principal, rate, time)
                calculation_type = 'Compound Interest'
            elif choice == '2':
                result = loan_payment(principal, rate, time)
                calculation_type = 'Loan Payment'
            elif choice == '3':
                result = investment_return(principal, rate, time)
                calculation_type = 'Investment Return'
            elif choice == '4':
                present_value_input = data['present_value']
                result = future_value(present_value_input, rate, time)
                calculation_type = 'Future Value'
            elif choice == '5':
                future_value_input = data['future_value']
                result = present_value_input(future_value_input, rate, time)
                calculation_type = 'Present Value'
            else:
                result = 'Invalid Input'
                calculation_type = 'Invalid Input'

            print('Result:', result)
            print('Calculation Type:', calculation_type)

            context = {
                'result': result,
                'calculation_type': calculation_type
            }

            return render(request, 'calculator/index.html', context)

    else:
        form = PersonalFinanceForm()

    return render(request, 'calculator/index.html', {'form': form})
