# import this

# nuts = ['almond', 'pecan', 'cashew', 'brazil', 'walnut', 'pistachio']

# print(nuts[2:4])

# for nut in nuts:
#     print(nut)
    
# employees = ['bill', 'ted', 'rose', 'sarah', 'juan', 'crispin', 'sarah']
# employees.append('sussy baka')

# for name in employees:
#     print(f"I am so sorry that you had to find out this way {name.title()}, but you're fired. Actually {name.title()}, if I'm being honest, I never liked you very much anyways")

# thanos = "Dread it, run from it... Destiny arrives all the same."

# print(employees)
# print(employees.pop(3))
# print(employees)

guest_list = ['bill cosby', 'hitler', 'drew carey', 'your mom', 'diddle kid', 'lemon demon', 'watchdogman']

print(f"Unfortunately, it has been brought to my attention that {guest_list.pop(0).title()} has recently passed away, and will be unable to attend.")
guest_list.append("george w. bush")
print(f"While this is very sad, I am excited to announce that {guest_list[-1].title()} has been invited in their place!")
guest_list.insert(0, 'buck trungle')
guest_list.insert(len(guest_list)//2, 'david copperfield')
guest_list.append('tracer bullet')
print(guest_list)

print(f"Oh shit guys my parents found out and are very cross with me. They said I can only have two people over for dinner.")
while len(guest_list) > 2:
    print(f"Unfortunately, {guest_list.pop()}, you are not worthy of my time.")
    
for name in guest_list:
    print(f"Dear {name.title()},\n You are invited to my house for a party. Bring booze.")
    
del guest_list[0]
del guest_list[0]

print(guest_list)