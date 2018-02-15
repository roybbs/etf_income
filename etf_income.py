import argparse

parser = argparse.ArgumentParser(description='This script simply calculates the yearly income of an ETF, given a profit rate, an expense ratio, and # of dividends per year.')
parser.add_argument('-i', dest='initial_investment', type=float, required=True, help='An initial investment')
parser.add_argument('-p', dest='profit_rate', type=float, required=True, help='An annual profit rate you estimates (%)')
parser.add_argument('-e', dest='expense_ratio', type=float, required=True, help='An annual expense ratio (%)')
parser.add_argument('-t', dest='tax', type=float, required=True, help='A tax for expense ratio (%)')
parser.add_argument('-n', dest='num_dividends', type=int, required=True, help='The number of dividends per year')

def oneday(capital, profit_rate, expense_ratio):
  interest = capital * profit_rate / 365.0
  return (capital + interest)*(1.0-(expense_ratio/365.0))

args = parser.parse_args()

tax = args.tax
initial_investment = args.initial_investment
profit_rate = args.profit_rate /100.0
expense_ratio = args.expense_ratio *(1+(tax/100.0))/100.0
num_dividends = args.num_dividends

current_investment = initial_investment
income_gain  = 0
time_period_between_dividends = 365 / num_dividends
rest_of_days = 365 % num_dividends

print "initial_investment:", initial_investment
print "profit_rate:", profit_rate*100, "%"
print "expernse_ratio*tax:", expense_ratio*100, "%"
print "tax:", tax, "%"
print "num_dividends:", num_dividends
print "time_period:", time_period_between_dividends, "days"
print "rest_of_days:", rest_of_days, "day(s)"

for i in range(0,num_dividends):
  for j in range(0,time_period_between_dividends):
    current_investment = oneday(current_investment,profit_rate,expense_ratio)
  income_gain += current_investment - initial_investment
  current_investment = initial_investment

for i in range(0,rest_of_days):
  current_investment = oneday(current_investment,profit_rate,expense_ratio)
income_gain += current_investment - initial_investment

print "income_gain:", income_gain

