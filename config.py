from environs import Env

env = Env()
env.read_env()

TOKEN = env('TOKEN')
FROM_CHAT_ID_1 = env.list('FROM_CHAT_ID_1')
FROM_CHAT_ID_2 = env.list('FROM_CHAT_ID_2')
TO_CHAT_ID = env.int('TO_CHAT_ID')
TO_MESSAGE_THREAD_ID_1 = env.int('TO_MESSAGE_THREAD_ID_1')
TO_MESSAGE_THREAD_ID_2 = env.int('TO_MESSAGE_THREAD_ID_2')
