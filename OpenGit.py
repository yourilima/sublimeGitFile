import sublime, sublime_plugin
import webbrowser

class OpenGitCommand(sublime_plugin.WindowCommand):
    def run(self,edit):
        view = sublime.active_window().active_view()
        file = view.file_name()
        WindowCommand.open_new_tab('https://gitlab.prx.dk/%()s' % file)
