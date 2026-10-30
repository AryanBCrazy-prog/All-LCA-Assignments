import numpy as np
import pandas as pd
labels = ['a','b','c']
my_list = [10,20,30,999]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}
print(pd.Series(data=my_list))


import numpy as np
import pandas as pd
labels = ['a','b','c']
my_list = [10,20,30,999]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}
print(pd.Series(arr))


import numpy as np
import pandas as pd
labels = ['a','b','c']
my_list = [10,20,30,999]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}
print(pd.Series(arr,labels))


import numpy as np
import pandas as pd
labels = ['a','b','c']
my_list = [10,20,30,999]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}
print(pd.Series(d))


import numpy as np
import pandas as pd
labels = ['a','b','c']
my_list = [10,20,30,999]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}
print(pd.Series(data=labels))



ser1=pd.Series([1,2,3,4],index=['usa','germany','ussr','japan'])
print(ser1)

ser1=pd.Series([1,2,3,4],index=['usa','germany','ussr','japan'])
ser2=pd.Series([1,2,3,4],index=['usa','germany','ussr','japan'])
print(ser1+ser2)


import pandas as pd
import numpy as np
lst=['usa','germany','italy','japan']
ind=['a','b','c','d',]
df=pd.DataFrame(lst) #ind,['country']
print(df)

from numpy.random import randn
np.random.seed(101)
df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns = 'W X Y Z'.split())
print(df)


from numpy.random import randn
np.random.seed(101)
df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns = 'W X Y Z'.split())
print(df['W'])


from numpy.random import randn
np.random.seed(101)
df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns = 'W X Y Z'.split())
df['new']=df['W']+df['Y']
print(df)



import numpy as np
import pandas as pd
df=pd.DataFrame({'A':[1,2,np.nan],
                 'B':[5,np.nan,np.nan],
                 'C': [1,2,3]})
print(df)
