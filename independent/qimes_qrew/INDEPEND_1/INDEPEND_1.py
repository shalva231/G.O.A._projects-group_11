'''
=================================================
დავალება: მომხმარებელმა შეიყვანოს თავისი ნიშანი მათემატიკის და ქიმიის
თუ მას ჰქონდა 1-4 დაუწერე რომ დაბალი ნიშანი აქვს 
თუ ჰქონდა 5-8 დაუწერე რომ კარგი ნიშნები ყავს 
და თუ 9 ან ათო პქონდა დაუწერო რომ შესანიშნავი ნიშანი აქვს 
(გამოიყენე if , elif ასევე შეყვანილი ნიშნები სხვადასხვა იყოს)
=================================================
'''
#Get the marks from the user
math_marks = int(input("Enter your marks in Mathematics (1-10)>> "))
chemistry_marks = int(input("Enter your marks in Chemistry (1-10)>> "))

#performance in Mathematics
if math_marks <= 4:
    math_performance = "low"
elif 5 <= math_marks <= 8:
    math_performance = "good"
else:
    math_performance = "excellent"

#performance in Chemistry
if chemistry_marks <= 4:
    chemistry_performance = "low"
elif 5 <= chemistry_marks <= 8:
    chemistry_performance = "good"
else:
    chemistry_performance = "excellent"

#Provide feedback
print(f"In Mathematics, you have a {math_performance} mark.")
print(f"In Chemistry, you have a {chemistry_performance} mark.")
print(f"You did a {'good' if math_performance in ['good', 'excellent'] and chemistry_performance in ['good', 'excellent'] else 'not a good'} job.")