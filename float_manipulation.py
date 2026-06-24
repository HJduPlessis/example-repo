import statistics
import math

float_numbers=[];
sum=0;
for i in range(10):
    float_numbers.append(float(input("Enter float number: ")));
    sum+=float_numbers[i];

print(f'Total of all numbers: {sum}');
print(f'Maximum: {max(float_numbers)}');
print(f'Minimum: {min(float_numbers)}');
print(f'Rounded average: {round(sum/10,2)}')
print(f'Median: {statistics.median(float_numbers)}')