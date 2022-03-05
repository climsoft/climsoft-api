# gettext.install("climsoft_messages")
# gettext.bindtextdomain(
#     'climsoft_messages',
#     "/home/faysal/PycharmProjects/climsoft-api/src/climsoft_api/locale"
# )
# gettext.textdomain("climsoft_messages")
# _ = gettext.gettext

# fr = gettext.translation(
#     "climsoft_messages",
#     localedir="/home/faysal/PycharmProjects/climsoft-api/src/climsoft_api/locale",
#     languages=["fr"]
# )
# fr.install()
# _ = fr.gettext
# print(_("Successfully created station."))
#
# fr.install()

from babel.messages.frontend import compile_catalog

compiler = compile_catalog()
compiler.use_fuzzy = True
compiler.domain = ["climsoft_messages"]
# compiler.locale = "en"
compiler.directory = "/home/faysal/PycharmProjects/climsoft-api/src/climsoft_api/locale"
compiler.run()
# super().run()
