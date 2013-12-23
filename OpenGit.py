import sublime, sublime_plugin
import webbrowser,subprocess,re


class opengitCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		view = sublime.active_window().active_view()
		file = view.file_name()
		self.settings = sublime.load_settings('opengit.sublime-settings')
		# url = self.getOpenGitUrl(settings.get('opengit_url'))
		file = file.replace('{}/'.format(self.getGitPath()),'')
		branch = self.getBranch()
		origin = self.getOrigin()
		if(not origin):
			return
		webbrowser.open_new_tab('{}/blob/{}/{}'.format(origin,branch,file))
	
	def getBranch(self):
		p = subprocess.Popen('git branch --no-color|grep "^* "', stdout=subprocess.PIPE, shell=True)
		(output,error) = p.communicate()
		branch = re.search('^\* (\w+)',output.decode('utf-8'))
		return ''.join(branch.group(1).split('\n'))

	def getOrigin(self):
		p = subprocess.Popen('git remote -v|grep fetch', stdout=subprocess.PIPE, shell=True)
		(output,error) = p.communicate()
		originurl = re.search('(http(s)?://(.)*) (\(fetch\))',output.decode('utf-8'))
		if(originurl is not None):
			url = originurl.group(1)
			url = url.replace('.git','')
			return url
		originurl = re.search('(:(.*)\.git) (\(fetch\))',output.decode('utf-8'))
		if(originurl is not None):
			return '{}/{}'.format(self.getGitlabUrl(self.settings.get('gitlab_url')),originurl.group(2))
		return False

	def getGitlabUrl(self,default = 'http://localhost'):
		settings = self.getProjectSettings()
		if ('gitlab_url' not in settings):
			return default
		return settings['gitlab_url']

	def getGitPath(self):
		p = subprocess.Popen('git rev-parse --show-toplevel', stdout=subprocess.PIPE, shell=True)
		(output,error) = p.communicate()
		return ''.join(output.decode('utf-8').split('\n'))

	def getOpenGitUrl(self,default):
		window = sublime.active_window()
		project = window.project_data()
		if (project is None) or ('settings' not in project):
			return []
		folders = window.folders()
		project_data = project['settings']
		index = 0
		ready_settings = []

		for folder in folders:
			if 'opengit' not in project_data[index]:
				index += 1
				continue

			project_folder = project_data[index]['opengit']
			project_folder['source'] = folder
			if 'opengit_url' not in project_folder:
				opengit_url = default
				print(opengit_url)
				project_folder['opengit_url'] = opengit_url

			ready_settings.append(project_folder)
			index += 1

		return ready_settings

	def getProjectSettings(self):
		window = sublime.active_window()
		project = window.project_data()
		if (project is None) or ('settings' not in project):
			return []
		return project['settings']