from sqlalchemy import create_engine


engine = create_engine('sqlite:text_editor.db', echo=True)

