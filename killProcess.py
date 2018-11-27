import argparse
import os
import re
def main():
    parser = argparse.ArgumentParser(description='process killer')
    parser.add_argument('-p',dest='port',help='The process will be killed')
    options = None
    try:
        options = parser.parse_args()
    except:
        print('error')
        exit(0)
    if options.port !=None:
        port = str(options.port).split(',')
        for p in port:
            result = os.popen('netstat -ano|findstr '+p, 'r')
            res = result.read()
            print('netstat -ano|findstr '+p)
            print(res)
            print('----------------------------------')
            if res!=None:
                res2 = res.split('\n')
                s = set()
                for x in res2:
                    res3 = [y for y in x.split(' ') if y.isdigit()]
                    if len(res3)==1:
                        if s.issuperset(res3):
                            continue
                        else:
                            s = s.union(res3)
                            try:
                                print('Kill this process in port:'+res3[0])
                                r = os.system('taskkill /f /pid ' + res3[0])
                                if(r==0):
                                    print('Process in port '+res3[0]+' has been killed success')
                            except:
                                print('Kill process in port'+res3[0]+'failed')  
    else:
        print('Please input the port of process!')         

if __name__ == '__main__':
    main()