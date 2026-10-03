name = input("Enter your real name:")
gadget = input("Enter your favourite gadget:")

agent_number = 7
speed_raiting = 9.5
mission_count = 5
height_m = 1.5
is_active = True

print("name", name,"type ->",type(agent_number))
print("gadget", gadget,"type ->",type(gadget))
print("agent_number", agent_number,"type ->",type(agent_number))
print("speed_raiting", speed_raiting,"type ->",type(speed_raiting))
print("mission_count", mission_count,"type ->",type(mission_count))
print("is_active", is_active,"type ->",type(is_active))



first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First Three Leters of name", first_three)
print("Last letter of name", last_letter)
print("Secret Code Name", code_name)

reversed_gadget = gadget[::-1]
print("Reversed Gadget Name:", reversed_gadget)


badge_line_1 = "AGENT" + code_name.upper()
badge_line_2 = "ID:" + str(agent_number) + "MISSIONS:" + str(mission_count)
badge_line_3 = "SPEED" + str(speed_raiting) + "ACTIVE: " + str(speed_raiting)
badge_line_4 = "SECRET GADGET CODE:" + reversed_gadget.upper()
