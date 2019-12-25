This is a Python3, working version of the [pydpi-1-0](https://pypi.org/project/pydpi/) library.

The following modyfications were made:           
1. `2to3` was applied     
2. tabs were converted to 4spaces with `tabs2spaces.py` [code](https://gist.github.com/antivanov/59e00f6129725e9b4404)     
3. `black` was used     
4. `string.strip(X) --> X.strip()`        
5. `string.replate() --> str.replace()`         
6. Started changing print to logging.info()     

### INSTALL
1. Go the the py3dpi repository:      
`cd external/py3dpi`    
2. Run the installation script:      
`sudo python setup.py install`     
3. Test the installation:      
`...`


### TODO:
1. Refactor and cleanup code      
2. `flake8`      
3. Debug and make more user friendly      

### License
GPL

Contact me at gniewko.pablo@gmail.com for questions.

