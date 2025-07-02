# 14_exception_handling_flow.py
# --------------------------------------------------------------------
# This script demonstrates the use of try-except-else-finally blocks
# to handle exceptions and ensure proper flow control

try:
    a = int(input("Enter a number: "))
    print(f"Number is {a}")

except Exception as e:
    print("❌ Please enter an integer.")
    print("Error:", e)

else:
    print("✅ You did a great job! No errors occurred.")

finally:
    print("🔚 I will always run (finally block).")
