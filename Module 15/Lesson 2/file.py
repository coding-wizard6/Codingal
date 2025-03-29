with open ('new.txt','w') as f:
    f.write("India is a beautiful land with a variety of wildlife and rich cultural diversity. The Bengal Tiger is considered the national animal of India. India celebrates its Independence Day on 15th August every year. It is observed to commemorate the freedom of India from the British. The tri-coloured national flag is called Tiranga, designed with saffron, white and green with the Ashok Chakra in navy blue at the centre of the flag. ‘Lion Capital of Ashoka’ is the country’s national emblem. The national motto is ‘Satyameva Jayate,’ which means truth alone wins.")
f.close()

with open ('new.txt','r') as f:
    data=f.readlines()
    for lines in data:
        words=lines.split()
        print(words)
f.close()