from instagpy import InstaGPy

username = "predator_mmm"
insta = InstaGPy(use_mutiple_account=False, session_ids=None, min_requests=None, max_requests=None)
txt = insta.get_user_basic_details(username)
print(txt)