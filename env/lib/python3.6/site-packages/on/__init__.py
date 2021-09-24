import os
from on.util import ModuleNotFoundIgnore

file_sep = os.path.sep

from on.util import lazyprop, groupby, regroupby, igroupby
from on.trans import add_ipython_key_completions

# Imports to be able to easily get started...
from on.base import (
    Collection,
    KvReader,
    KvPersister,
    Reader,
    Persister,
    kv_walk,
)

from on.base import Store

from on.trans import (
    wrap_kvs,
    disable_delitem,
    disable_setitem,
    mk_read_only,
    kv_wrap,
    cached_keys,
    filt_iter,
    filtered_iter,
    add_path_get,
    insert_aliases,
)


def kvhead(store, n=1):
    """Get the first item of a kv store, or a list of the first n items"""
    if n == 1:
        for k in store:
            return k, store[k]
    else:
        return [(k, store[k]) for i, k in enumerate(store) if i < n]


def ihead(store, n=1):
    """Get the first item of an iterable, or a list of the first n items"""
    if n == 1:
        for item in iter(store):
            return item
    else:
        return [item for i, item in enumerate(store) if i < n]
