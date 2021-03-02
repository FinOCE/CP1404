"""
bloggers question (using twitter_users.txt)
"""
def main():
    with open('twitter_users.txt', 'r') as file:
        header = file.read().split('\n')[0]
        file = open('twitter_users.txt', 'r')
        bloggers = [line.strip() for i, line in enumerate(file) if i > 0]
        for i, blogger in enumerate(bloggers):
            name = blogger.split(',')[0]
            creation_date = tuple(blogger.split(',')[1].split(':')[::-1])
            followers_count = int(blogger.split(',')[2])
            
            bloggers[i] = [name, creation_date, followers_count]
        bloggers = sorted(bloggers, key=sort_by_followers)
    
    with open('bloggers.txt', 'w') as file:
        content = f'{header}\n'
        for blogger in bloggers:
            content += f'{blogger[1][0]}-{blogger[1][1]}-{blogger[1][2]} = {blogger[0]}:{blogger[2]}\n'
        file.write(content)

def sort_by_followers(value):
    return value[2]

if __name__ == '__main__':
    main()