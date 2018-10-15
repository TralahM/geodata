#!/data/data/com.termux/files/usr/bin/env python
from parsecounty import counties,subcounties
from constituencies import constituencies
class Kenya(object):
    _Counties=counties
    _Subcounties=subcounties
    _Constituencies=constituencies
    def get_county_by_code(code):
        if isinstance(code,int) and abs(code)<=47 and abs(code)>0:
            return Kenya._Counties[code]
        else:
            raise Exception
    def get_county_by_name(name):
        if isinstance(name,str):
            #name=name.upper()
            if name in Kenya._Counties.values():
                for k in Kenya._Counties:
                    if Kenya._Counties[k]==name:
                        return (k,name)
            else:
                raise Exception
        else:
            raise TypeError("String Value Required!")
    def get_subcounties_by_county_code(code):
        if isinstance(code,int) and abs(code)>0 and abs(code)<=47:
            return Kenya._Subcounties[code]
        else:
            raise Exception
    def get_county_by_subcounty_name(name):
        if isinstance(name,str):
            #name=name.upper()
            for i in range(1,48):
                if name in Kenya._Subcounties[i]:
                    return Kenya._Counties[i]
        else:
            raise TypeError("String Value Required!")
        
    def get_subcounties_by_county_name(name):
        if isinstance(name,str):
            #name=name.upper()
            k,v=Kenya.get_county_by_name(name)
            return (name,Kenya._Subcounties[k])
        else:
            raise TypeError("String Value Required!")
    @property
    def county_number():
        return len(Kenya._Counties)
    
    def get_subcounty_number(keyw='all'):
        if isinstance(keyw,int) and abs(keyw)>0 and abs(keyw)<=47:
            return len(Kenya.get_subcounties_by_county_code(keyw)[1])
        elif isinstance(keyw,str):
            #keyw=keyw.upper()
            if keyw=='ALL':
                g=map(len,Kenya._Subcounties.values())
                cnt=[next(g) for i in range(47)]
                return sum(cnt)
            else:
                return len(Kenya.get_subcounties_by_county_name(keyw)[1])
        else:
            raise TypeError("Integer or String Value Required!")
    def __str__():
        return "Welcome to the Country Kenya!\nHere are some statistics about the country:\n\t\tKenya has %d Counties.\n\t\tIt has %d Subcounties.\n\t\tThe Capital is Nairobi.\n\n"
    def __repr__():
        return str(Kenya)
    
        
        
            
