#!/data/data/com.termux/files/usr/bin/env python
from parsecounty import counties,subcounties
from constituencies import constituencies
from colorify import colorfg
class Kenya:
    _Counties=counties
    _Subcounties=subcounties
    _Constituencies=constituencies


    def get_county_by_code(code):
        if isinstance(code,int) and abs(code)<=47 and abs(code)>0:
            return Kenya._Counties[code]
        else:
            raise ValueError("Integer between 1 and 47 Required!")


    def get_county_by_name(name):
        if isinstance(name,str):
            if name[-1]!=' ':
                name+=" "
            name=name.upper()
            if name in Kenya._Counties.values():
                for k in Kenya._Counties:
                    if Kenya._Counties[k]==name:
                        return (k,name)
            else:
                raise ValueError("%s not a County"%name)
        else:
            raise TypeError("String Value Required!")


    def get_subcounties_by_county_code(code):
        if isinstance(code,int) and abs(code)>0 and abs(code)<=47:
            return Kenya._Subcounties[code]
        else:
            raise ValueError("Integer between 1 and 47 Required!")


    def get_county_by_subcounty_name(name):
        if isinstance(name,str):
            name=name.upper()+" "
            for i in range(1,48):
                if name in Kenya._Subcounties[i]:
                    return Kenya._Counties[i]
        else:
            raise TypeError("String Value Required!")
        

    def get_subcounties_by_county_name(name):
        if isinstance(name,str):
            name=name.upper()
            k,v=Kenya.get_county_by_name(name)
            return Kenya._Subcounties[k]
    
    def get_subcounties_by_constituency_name(name):
        return Kenya.get_subcounties_by_county_name(Kenya.get_county_by_constituency_name(name))
    def county_number():
        return len(Kenya._Counties)
    


    def get_subcounty_number(keyw='all'):
        if isinstance(keyw,int) and abs(keyw)>0 and abs(keyw)<=47:
            return len(Kenya.get_subcounties_by_county_code(keyw)[1])
        elif isinstance(keyw,str):
            keyw=keyw.upper()
            if keyw=='ALL':
                g=map(len,Kenya._Subcounties.values())
                cnt=[next(g) for i in range(47)]
                return sum(cnt)
            else:
                return len(Kenya.get_subcounties_by_county_name(keyw)[1])
        else:
            raise TypeError("Integer or String Value Required!")

    
    def get_constituencies_by_county_code(code):
        if isinstance(code,int) and abs(code)>0 and abs(code)<=47:
            return (code,Kenya._Constituencies[Kenya._Counties[code]])
        else:
            raise ValueError("Integer between 1 and 47 Required!")

    def get_constituencies_by_county_name(name):
        if isinstance(name,str):
            name=name.upper()
            return Kenya._Constituencies[Kenya.get_county_by_name(name)[1]]
        else:
            raise TypeError("String Value Required!")
    def get_county_by_constituency_name(name):
        if isinstance(name,str):
            name=name.upper()
            for key,val in Kenya._Constituencies.items():
                if name in val:
                    return Kenya.get_county_by_name(key)[1]
        else:
            raise TypeError("String Value Required!")


    def get_constituency_number(keyw):
        if isinstance(keyw,int) and abs(keyw)>0 and abs(keyw)<=47:
            return len(Kenya.get_constituencies_by_county_code(keyw)[1])
        elif isinstance(keyw,str):
            keyw=keyw.upper()
            if keyw=='ALL':
                g=map(len,Kenya._Constituencies.values())
                cnt=[next(g) for i in range(47)]
                return sum(cnt)
            else:
                return len(Kenya.get_constituencies_by_county_name(keyw)[1])
        else:
            raise TypeError("Integer or String Value Required!")

    
    def get_constituencies_by_county_code(code):
        if isinstance(code,int) and abs(code)>0 and abs(code)<=47:
            return Kenya._Constituencies[Kenya._Counties[code]]
        else:
            raise ValueError("Integer between 1 and 47 Required!")

    def get_constituencies_by_subcounty_name(name):
        if isinstance(name,str):
            return Kenya.get_constituencies_by_county_name(Kenya.get_county_by_subcounty_name(name))
        else:
            raise TypeError("String Value Required!")
    def get_county_by_constituency_name(name):
        if isinstance(name,str):
            name=name.upper()
            for key,val in Kenya._Constituencies.items():
                if name in val:
                    return Kenya.get_county_by_name(key)[1]
        else:
            raise TypeError("String Value Required!")

    
    def __str__():
        return colorfg("Welcome to the Country Kenya!\nHere are some statistics about the country:\n\t\tKenya has %d Counties.\n\t\tIt has %d Subcounties.\n\t\tThe Capital is Nairobi.\n\t\tKenya has %s Constituencies.\n\n")%(47,Kenya.get_subcounty_number('all'),290)

    
    def info():
        print(Kenya.__str__())
