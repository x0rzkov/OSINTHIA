lognum = 3
lognext = 1



def loggit():          
    from time import strftime
    
    
                  
    logdatetime = strftime("%m%d%Y%H%M")

    where = raw_input('What is your physical location?\t')
    city = raw_input('What city are you in?\t')
    what = raw_input('What are you doing?\t')

    
    
    logtracker = '%s %s %s, TX-log %s| %s.' %  (logdatetime, where, city, lognum, what)
    logtrackgit = 'git commit -m "%s"' % logtracker
    
    file = 'loggitlogslogs.log'
    location = './loggitlogs/%s' % file
    string = open(location, 'a+')
    
    endlogg = '%s\n\n' % logtracker
    string.write('%s' % endlogg)
    string.close()
    
    print(logtracker)
    
    return


def logchange():
    task = raw_input('Proceed as usual? ')
    if task == 'no':
        with open(__file__, 'r') as f: 
            lines = f.read().split('\n')
            val = int(lines[0].split(' = ')[-1])
            new_line = 'lognum = {}'.format(val-1)
            new_file = '\n'.join([new_line] + lines[1:])

        with open(__file__, 'w') as f:
            f.write('\n'.join([new_line] + lines[1:]))
            
        return
    else:
        with open(__file__, 'r') as f: 
            lines = f.read().split('\n')
            val = int(lines[0].split(' = ')[-1])
            new_line = 'lognum = {}'.format(val+1)
            new_file = '\n'.join([new_line] + lines[1:])

        with open(__file__, 'w') as f:
            f.write('\n'.join([new_line] + lines[1:]))
        loggit()
        
        return


logchange()





