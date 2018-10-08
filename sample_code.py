'''
import wx

app = wx.App()

frame = wx.Frame(None, -1)
frame.Show()

app.MainLoop()
'''
'''
import wx


class MyApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        self.SetTitle('タイトル')
        self.SetBackgroundColour((255, 0, 0))
        self.SetPosition((200, 100))
        self.SetSize((400, 300))
        self.Show()


app = wx.App()
MyApp(None)
app.MainLoop()
'''
'''
import wx


class MyApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        self.SetTitle('タイトル')
        self.SetBackgroundColour((255, 0, 0))
        self.SetPosition((600, 100))
        self.SetSize((450, 350))
        self.Show()

        panel_G = wx.Panel(self, -1, pos=(10, 10), size=(180, 260))
        panel_G.SetBackgroundColour((0, 255, 0))

        panel_B = wx.Panel(self, -1)
        panel_B.SetBackgroundColour((0, 0, 255))
        panel_B.SetPosition((210, 10))
        panel_B.SetSize((180, 260))


app = wx.App()
MyApp(None)
app.MainLoop()
'''
'''
import wx


class MyApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        self.SetTitle('ラベル')
        self.SetSize((400, 300))
        self.Show()

        panel_ui = wx.Panel(self, -1, pos=(50, 50), size=(300, 200))

        label_jp = wx.StaticText(panel_ui, -1, 'こんにちは。', pos=(10, 10))
        label_en = wx.StaticText(panel_ui, -1, '', pos=(10, 50))
        label_en.SetLabel('Hello.')


app = wx.App()
MyApp(None)
app.MainLoop()
'''
'''
import wx


class MyApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        self.SetTitle('ラベル')
        self.SetSize((400, 300))
        self.Show()

        panel_ui = wx.Panel(self, -1, pos=(50, 50), size=(300, 200))

        self.label = wx.StaticText(panel_ui, -1, 'こんにちは。', pos=(10, 10))

        btn = wx.Button(panel_ui, -1, '変換', pos=(10, 50))
        btn.Bind(wx.EVT_BUTTON, self.clicked)

    def clicked(self, event):
        self.label.SetLabel('Hello.')


app = wx.App()
MyApp(None)
app.MainLoop()
'''
import wx


class MyApp(wx.Frame):

    def __init__(self, *args, **kw):
        super(MyApp, self).__init__(*args, **kw)

        self.init_ui()

    def init_ui(self):
        self.SetTitle('テキストボックス')
        self.SetSize((400, 300))
        self.Show()

        panel_ui = wx.Panel(self, -1, pos=(50, 50), size=(300, 200))

        self.label = wx.StaticText(panel_ui, -1, '', pos=(10, 10))

        self.box = wx.TextCtrl(panel_ui, -1, pos=(10, 50))

        btn = wx.Button(panel_ui, -1, 'コピー', pos=(10, 90))
        btn.Bind(wx.EVT_BUTTON, self.clicked)

    def clicked(self, event):
        text = self.box.GetValue()
        self.box.Clear()
        self.label.SetLabel(text)


app = wx.App()
MyApp(None)
app.MainLoop()