#Analytical thinking and boolean logic 
#Movie Theater Entry Check 

##**Activity 1:Idenbtify the Components**
###What are the inputs?
**Answer.**
```
-`age` - integer 
-`accompanied_by_adult`-boolean 
- `has_valid_ticket` - boolean
```

###What is the Process?
**Answer.**
```
Apply the admission rule:
1.Check if age >= 13 then set`age_ok = true/False`
2.If age_ok is False, check if accompanied_by_adult is True then set 'adult_ok = True/False'
3.Compute `entry_condition = (age_ok OR adult_ok)`
4.Finally, `entry_allowed = entry_condition AND has_valid_ticket` 
```

##output
```
- Boolean value: `True` (allow entry) or `Faslse` (deny entry)
```

---
##**Activity 2: Design the Algorithm:**
--

###The Flow
![alt text](<Screenshot 2026-06-10 123605.png>)

##The truth Table

###The Truth Table

| Age ≥ 13 | With Adult | Has Ticket | Entry Allowed |
|-----------|------------|------------|---------------|
| True      | True       | True       | True          |
| True      | False      | True       | True          |
| False     | True       | True       | True          |
| False     | False      | True       | False         |



###Algorithm(The Step-by-Step Solution)
**Answer**
1.Start
2.Read age, accompanied_by_adult (yes/no), has_valid_ticket (yes/no)
3.Set eligible = False
4.If age >= 13 then set eligible = True, else if accompanied_by_adult = yes then set eligible = True
5.Evaluate conditons: If eligible = Trie AND has_valid_ticket = yes then allow entry, else deny entry
6.Display result
7.End



###Pseudocode
**Answer:**
START 
    INPUT age 
    INPUT accompanied_by_adult
    INPUT has_valid_ticket 
    eligible = FALSE 
    IF age >= 13 THEN 
        eligibile = True
    ELSE IF accompanied_by_adult == True
THEN 
        eligible = True
    END IF

    IF eligible == True AND 
    has_valid_ticket == True THEN 
        OUTPUT  "Allow entry"
    ELSE
        OUTPUT "Deny entry"
    END IF
END


