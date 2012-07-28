def create(c):
    from .. import tables
    tables.Base.metadata.create_all(c)