##  Disclaimer
I take not responsibility for your use of the software. Development is done in my personal capacity and carry no affiliation to my work.

# ShareAttack!
*Crawl any windows network with Active Directory for computers and subsequently launch an attack on weak file permissions.*

__Usage__: Run ShareAttack!.py, ensure DSQUERY and SHARELOCATOR are included in the same root folder.

__Synops:__ This attack exploits weak file permissions allowing users to overwrite file permissions assigned to file shares.
Instead of exploiting file shares to gain access, the attack focuses on DENYING access to file shares. The attack uses the exploited account's credentials, (administrator account will be much more powerful). 

__Files:__ 
* ShareAttack!.py (_main file to launch attack_)
* dsquery.exe (_standard DSQUERY to extract AD computers_) https://technet.microsoft.com/en-us/library/cc732952(v=ws.11).aspx
* sharelocator.exe (_Extract file shares from target server using srvsvc.NetShareEnumAll MSRPC function and then apply deny   permissions (C++ please request source)_)

__Walkthrough:__
1. Load files onto target.
2. Execute ShareAttack!.py
3. Will automatically execute dsquery command to extract domain computers.
4. Test computers and retain active hosts.
5. Pass active computers onto ShareLocator.
6. ShareLocator will find all fileshares on target.
7. Attempt to apply DENY permission for each user with access.

__Requirements:__
* Windows computer environment, with AD for dsquery.
* Python 3.6 feel free to port, reference GIT please.
* Weak file permissions :P

__Version:__ 0.1       

__Parameters:__ *$crawl_limit*: set amount of computers to extract from AD, 0 extracts all.

__Alternatives [future to-do]:__
* ShareAttack!.py not required, can use only sharelocator.exe ```Sharelocator <servername>```
* Replace DSQUERY with IP range or provide option to user at startup
* Port .py to Windows

__Note that non lethal version is uploaded, please msg to request lethal version__

