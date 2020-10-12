lognum = 2
lognext = 1



def loggit():          
    from time import strftime
    
    
                  
    logdatetime = strftime("%m%d%Y%H%M")

    where = raw_input('What is your physical location?\t')
    feeling = raw_input('On a scale of 1 - 10, how are you feeling right now?\t')
    what = raw_input('What are you doing?\t')

    
    
    logtracker = '%s %s %s, OSINTHIA-log %s| %s.' %  (logdatetime, where, feeling, lognum, what)
    logtrackgit = 'git commit -m "%s"' % logtracker
    
    ####Below is part of a logging project to log everything (I'm sure a program exists but I like doing things on my own)
    ####but I am pausing that to work on OSINTHIA.

    #file = 'loggitlogslogs.log'
    #location = './loggitlogs/%s' % file
    #string = open(location, 'a+')
    
    #endlogg = '%s\n\n' % logtracker
    #string.write('%s' % endlogg)
    #string.close()
    
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





