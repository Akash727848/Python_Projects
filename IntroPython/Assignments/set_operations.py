s1={'a','k','a','s','h'}
s2=set(s1)
#print(s2)
s3={'m','o','u','n','i','c','a'}
#print(s3)
#print(s2.union(s3))
s4=s2.intersection(s3)
print(s4)
s2.intersection_update(s3)
print(s2)