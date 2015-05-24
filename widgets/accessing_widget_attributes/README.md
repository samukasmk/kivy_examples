
Kivy docs reference:
```
http://kivy.org/docs/guide/lang.html#accessing-widgets-defined-inside-kv-lang-in-your-python-code
```

#Accessing Widgets defined inside Kv lang in your python code
--
Consider the code below in my.kv:

``` yaml
<MyFirstWidget>:
    # both these variables can be the same name and this doesn't lead to
    # an issue with uniqueness as the id is only accessible in kv.
    txt_inpt: txt_inpt
    Button:
        id: f_but
    TextInput:
        id: txt_inpt
        text: f_but.state
        on_text: root.check_status(f_but)
```
In myapp.py:

``` python
class MyFirstWidget(BoxLayout):

    txt_inpt = ObjectProperty(None)

    def check_status(self, btn):
        print('button state is: {state}'.format(state=btn.state))
        print('text input text is: {txt}'.format(txt=self.txt_inpt))
```

txt_inpt is defined as a ObjectProperty initialized to None inside the Class.:

txt_inpt = ObjectProperty(None)
At this point self.txt_inpt is None. In Kv lang this property is updated to hold the instance of the TextInput referenced by the id txt_inpt.:

txt_inpt: txt_inpt
From this point onwards, self.txt_inpt holds a reference to the widget identified by the id txt_input and can be used anywhere in the class, as in the function check_status. In contrast to this method you could also just pass the id to the function that needs to use it, like in case of f_but in the code above.

There is a simpler way to access objects with id tags in Kv using the ids lookup object. You can do this as follows:

``` yaml
<Marvel>
  Label:
    id: loki
    text: 'loki: I AM YOUR GOD!'
  Button:
    id: hulk
    text: "press to smash loki"
    on_release: root.hulk_smash()
```

In your python code:

``` python
class Marvel(BoxLayout):

    def hulk_smash(self):
        self.ids.hulk.text = "hulk: puny god!"
        self.ids["loki"].text = "loki: >_<!!!"  # alternative syntax
```

When your kv file is parsed, kivy collects all the widgets tagged with id’s and places them in this self.ids dictionary type property. That means you can also iterate over these widgets and access them dictionary style:

``` python
for key, val in self.ids.items():
    print("key={0}, val={1}".format(key, val))
```

> Note:
> Although the self.ids method is very concise, it is generally regarded as ‘best practise’ to use the ObjectProperty. This creates a direct reference, provides faster access and is more explicit.
