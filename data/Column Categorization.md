# TEDS-A Appendix A Columns Categorized

Understanding the type of data available. This will form the basis of how I will model the data in the future into tables using DuckDB.

## 1. Identification and Admission Details
1. **CASEID**: Case identification number
2. **ADMYR**: Year of admission

## 2. Demographic Information
3. **AGE**: Age at admission
4. **GENDER**: Gender
5. **RACE**: Race
6. **ETHNIC**: Ethnicity
7. **MARSTAT**: Marital status
8. **EDUC**: Education

## 3. Employment and Economic Information
9. **EMPLOY**: Employment status
10. **PRIMINC**: Source of income/support
11. **DETNLF**: Detailed not in labor force
12. **PRIMPAY**: Primary source of payment for treatment
13. **HLTHINS**: Health insurance

## 4. Living Situation and Legal Information
14. **LIVARAG**: Living arrangements
15. **ARRESTS**: Arrests in past 30 days
16. **DETCRIM**: Detailed criminal justice referral

## 5. Health and Special Status
17. **PREG**: Pregnant at admission
18. **VET**: Veteran status
19. **PSYPROB**: Co-occurring mental and substance use disorders

## 6. Substance Use Information
20. **SUB1**: Substance use (primary)
21. **ROUTE1**: Route of administration (primary)
22. **FREQ1**: Frequency of use (primary)
23. **FRSTUSE1**: Age at first use (primary)
24. **SUB2**: Substance use (secondary)
25. **ROUTE2**: Route of administration (secondary)
26. **FREQ2**: Frequency of use (secondary)
27. **FRSTUSE2**: Age at first use (secondary)
28. **SUB3**: Substance use (tertiary)
29. **ROUTE3**: Route of administration (tertiary)
30. **FREQ3**: Frequency of use (tertiary)
31. **FRSTUSE3**: Age at first use (tertiary)
32. **IDU**: Current IV drug use reported at admission

## 7. Substance Use Flags
33. **ALCFLG**: Alcohol reported at admission
34. **COKEFLG**: Cocaine/crack reported at admission
35. **MARFLG**: Marijuana/hashish reported at admission
36. **HERFLG**: Heroin reported at admission
37. **METHFLG**: Non-rx methadone reported at admission
38. **OPSYNFLG**: Other opiates/synthetics reported at admission
39. **PCPFLG**: PCP reported at admission
40. **HALLFLG**: Hallucinogens reported at admission
41. **MTHAMFLG**: Methamphetamine/speed reported at admission
42. **AMPHFLG**: Other amphetamines reported at admission
43. **STIMFLG**: Other stimulants reported at admission
44. **BENZFLG**: Benzodiazepines reported at admission
45. **TRNQFLG**: Other tranquilizers reported at admission
46. **BARBFLG**: Barbiturates reported at admission
47. **SEDHPFLG**: Other sedatives/hypnotics reported at admission
48. **INHFLG**: Inhalants reported at admission
49. **OTCFLG**: Over-the-counter medication reported at admission
50. **OTHERFLG**: Other drug reported at admission

## 8. Geographic Information
51. **STFIPS**: Census state FIPS code
52. **CBSA2010**: CBSA 2010 code
53. **REGION**: Census region
54. **DIVISION**: Census division

## 9. Treatment Information
55. **SERVICES**: Type of treatment service/setting
56. **METHUSE**: Medication-assisted opioid therapy
57. **DAYWAIT**: Days waiting to enter substance use treatment
58. **PSOURCE**: Referral source
59. **NOPRIOR**: Previous substance use treatment episodes

## 10. Special Flags and Additional Information
60. **FREQ_ATND_SELF_HELP**: Frequency of attendance at self-help groups
61. **DSMCRIT**: DSM diagnosis (SuDS 4 or SuDS 19)
62. **ALCDRUG**: Substance use type

**Count of Columns: 62**

