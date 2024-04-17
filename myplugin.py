from tutormfe.hooks import MFE_APPS

@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["mymfe"] = {
        "repository": "https://github.com/ukozazenje/test-mfe.git",
        "port": 1995,# optional, will default to the Open edX current tag.
    }
    return mfes