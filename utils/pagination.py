#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'
from django.utils.safestring import mark_safe

# 翻页类
class Page:

        def __init__(self, current_page, data_count, per_page_count=10, pager_num=7):
            '''
            :param current_page: 当前页
            :param data_count: 数据总个数
            :param per_page_count: 每页显示默认值
            :param pager_num: 显示多少个页码默认值
            :return:
            '''
            self.current_page = current_page
            self.data_count = data_count
            self.per_page_count = per_page_count
            self.pager_num = pager_num

        @property  #@property 把函数变成属性，调用不用加()
        def start(self):
            return (self.current_page-1) * self.per_page_count

        @property
        def end(self):
            return self.current_page * self.per_page_count

        @property
        def total_count(self):
            '''
            :return: 返回总页码数
            '''
            v, y = divmod(self.data_count, self.per_page_count)
            if y:
                v += 1
            return v

        def page_str(self, base_url):
            # start_index = self.current_page - 5
            # end_index = self.current_page + 5 + 1
            page_list = []
            if self.total_count < self.pager_num:
                start_index = 1
                end_index = self.total_count+1
            else:
                if self.current_page <= (self.pager_num+1)/2:
                    start_index = 1
                    end_index = self.pager_num + 1
                else:
                    start_index = self.current_page - (self.pager_num-1)/2
                    end_index = self.current_page + (self.pager_num+1)/2
                    if (self.current_page + (self.pager_num-1)/2) > self.total_count:
                        end_index = self.total_count + 1
                        # 到最后，仍然显示10页
                        start_index = self.total_count - self.pager_num + 1
            # 上一页
            if self.current_page == 1:
                prev_page = '<a class="page" href="javascript:void(0)">上一页</a>'
            else:
                prev_page = '<a class="page" href="%s?p=%s">上一页</a>' % (base_url, self.current_page-1)
            page_list.append(prev_page)
            for i in range(int(start_index), int(end_index)):
                # 如果是当前页，加上active css配置
                if i == self.current_page:
                    templ = '<a class="page active" href="%s?p=%s">%s</a>' % (base_url, i, i)
                else:
                    templ = '<a class="page" href="%s?p=%s">%s</a>' % (base_url, i, i)
                page_list.append(templ)

            # 下一页
            if self.current_page == self.total_count:
                next_page = '<a class="page" href="#">下一页</a>'
            else:
                next_page = '<a class="page" href="%s?p=%s">下一页</a>' % (base_url, (self.current_page+1))
            page_list.append(next_page)
            # 跳转

            jump = """
            <input type="text" /><a style="margin:5px" onclick="jumpTo(this, );" id="ii1">GO</a>
            <script>
                function jumpTo(ths){
                    var val = ths.previousSibling.value;
                    location.href = "%s?p=" + val
                }
            </script>
            """ % (base_url)

            page_list.append(jump)
            print(page_list)
            page_str = mark_safe(" ".join(page_list))
            page_str = mark_safe(page_str)
            return page_str