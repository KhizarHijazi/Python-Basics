"""Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)."""

score = int(input("Enter your score :"))

if score > 100 :
    print("not a vlid score") 
elif score >= 90:
    print("you got A Grade")
elif score >= 80 :
    print("you got B Grade")
elif score >= 70 :
    print("you got C Grade")
elif score >= 60 :
    print("you got D Grade")
elif score < 60 :
    print("your are failed")
