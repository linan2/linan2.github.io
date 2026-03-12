#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Scholar Publications Updater
从Google Scholar抓取论文信息并生成HTML格式

作者: Li Nan
版本: 1.0
日期: 2025-03-12
"""

import json
import re
import sys
from datetime import datetime

try:
    from scholarly import scholarly
except ImportError:
    print("❌ 错误: 未安装scholarly库")
    print("请运行: pip install scholarly")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ 错误: 未安装beautifulsoup4库")
    print("请运行: pip install beautifulsoup4")
    sys.exit(1)


class GoogleScholarUpdater:
    def __init__(self, author_name, affiliation):
        """
        初始化Google Scholar更新器

        参数:
            author_name: 作者姓名 (例如: "Nan Li")
            affiliation: 所属机构 (例如: "Tianjin University")
        """
        self.author_name = author_name
        self.affiliation = affiliation
        self.publications = []
        self.author_info = {}

    def search_author(self):
        """搜索并获取作者信息"""
        print(f"🔍 正在搜索作者: {self.author_name} ({self.affiliation})...")

        try:
            # 搜索作者
            search_query = scholarly.search_author(f'{self.author_name} {self.affiliation}')
            author = next(search_query)

            # 获取详细信息
            print(f"✅ 找到作者: {author.get('name', 'Unknown')}")
            print(f"   所属机构: {author.get('affiliation', 'Unknown')}")
            print(f"   引用总数: {author.get('citedby', 0)}")

            self.author_info = {
                'name': author.get('name', ''),
                'affiliation': author.get('affiliation', ''),
                'citedby': author.get('citedby', 0),
                'hindex': author.get('hindex', 0),
                'i10index': author.get('i10index', 0)
            }

            # 获取完整信息
            author = scholarly.fill(author)

            return author

        except StopIteration:
            print(f"❌ 错误: 未找到作者 '{self.author_name}'")
            return None
        except Exception as e:
            print(f"❌ 错误: {str(e)}")
            return None

    def fetch_publications(self, author, max_papers=20):
        """
        获取论文列表

        参数:
            author: 作者信息
            max_papers: 最大论文数量
        """
        print(f"📄 正在获取论文列表 (最多{max_papers}篇)...")

        publications = []

        for i, pub in enumerate(author['publications'][:max_papers]):
            try:
                print(f"   正在获取第 {i+1} 篇: {pub['bib']['title'][:50]}...")

                # 获取论文详细信息
                pub_filled = scholarly.fill(pub)

                # 提取信息
                bib = pub_filled['bib']
                publication = {
                    'title': bib.get('title', ''),
                    'authors': bib.get('author', ''),
                    'venue': bib.get('venue', ''),
                    'year': bib.get('pub_year', ''),
                    'volume': bib.get('volume', ''),
                    'issue': bib.get('issue', ''),
                    'pages': bib.get('pages', ''),
                    'publisher': bib.get('publisher', ''),
                    'abstract': bib.get('abstract', ''),
                    'citations': pub_filled.get('num_citations', 0)
                }

                publications.append(publication)

            except Exception as e:
                print(f"   ⚠️  跳过第 {i+1} 篇 (错误: {str(e)})")
                continue

        print(f"✅ 成功获取 {len(publications)} 篇论文")
        self.publications = publications
        return publications

    def categorize_papers(self):
        """
        分类论文：期刊论文和会议论文

        返回:
            journals: 期刊论文列表
            conferences: 会议论文列表
        """
        journals = []
        conferences = []

        # 常见的期刊关键词
        journal_keywords = [
            'journal', 'transactions', 'letters', 'review', 'science', 'applications',
            'communications', 'processing', 'speech communication', 'signal processing',
            'neural networks', 'expert systems', 'acoustics'
        ]

        # 常见的会议关键词
        conference_keywords = [
            'conference', 'proceedings', 'international', 'annual',
            'icassp', 'interspeech', 'iconip', 'ijcnn', 'icml', 'neurips',
            'congress', 'symposium', 'workshop', 'meeting'
        ]

        for pub in self.publications:
            venue = pub['venue'].lower() if pub['venue'] else ''
            title = pub['title'].lower() if pub['title'] else ''

            # 判断是期刊还是会议
            is_journal = any(keyword in venue for keyword in journal_keywords)
            is_conference = any(keyword in venue for keyword in conference_keywords)

            # 特殊处理：Speech Communication 是期刊
            if 'speech communication' in venue:
                is_journal = True
                is_conference = False

            # 特殊处理：ICASSP, INTERSPEECH 是会议
            if any(keyword in venue for keyword in ['icassp', 'interspeech']):
                is_conference = True
                is_journal = False

            if is_journal:
                journals.append(pub)
            elif is_conference:
                conferences.append(pub)
            else:
                # 无法判断，默认归类为期刊
                journals.append(pub)

        return journals, conferences

    def generate_html(self, output_file=None):
        """
        生成HTML格式的论文列表

        参数:
            output_file: 输出文件路径 (可选)

        返回:
            html_content: HTML内容
        """
        print("📝 正在生成HTML格式...")

        journals, conferences = self.categorize_papers()

        html_parts = []

        # 添加Google Scholar按钮
        html_parts.append('''
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 25px; border-radius: 10px; margin: 30px 0; text-align: center;">
                <h3 style="margin-bottom: 15px; border: none; color: white;">📚 Latest Publications</h3>
                <p style="margin-bottom: 20px; font-size: 1.1em;">My research papers are continuously updated on Google Scholar</p>
                <a href="https://scholar.google.com.hk/citations?user=9BVJbdsAAAAJ&hl=zh-CN" target="_blank"
                   style="background: white; color: #667eea; padding: 12px 30px; border-radius: 25px; text-decoration: none; font-weight: bold; display: inline-block; transition: all 0.3s;">
                    🔗 View All Papers on Google Scholar
                </a>
                <p style="margin-top: 15px; font-size: 0.9em; opacity: 0.9;">
                    Including papers from Expert Systems With Applications, Speech Communication, ICASSP, INTERSPEECH, and more
                </p>
            </div>
        ''')

        # 期刊论文
        if journals:
            html_parts.append('<h3 style="margin: 30px 0 15px 0; color: #667eea;">Journal Papers</h3>')

            for pub in journals:
                html_parts.append(self._format_journal_html(pub))

        # 会议论文
        if conferences:
            html_parts.append('<h3 style="margin: 30px 0 15px 0; color: #667eea;">Conference Papers</h3>')

            for pub in conferences:
                html_parts.append(self._format_conference_html(pub))

        html_content = '\n\n'.join(html_parts)

        # 保存到文件
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"✅ HTML内容已保存到: {output_file}")

        return html_content

    def _format_journal_html(self, pub):
        """格式化期刊论文HTML"""
        title = pub.get('title', '')
        authors = pub.get('authors', '')
        venue = pub.get('venue', '')
        year = pub.get('year', '')
        volume = pub.get('volume', '')
        issue = pub.get('issue', '')
        pages = pub.get('pages', '')
        citations = pub.get('citations', 0)

        # 生成期刊信息
        journal_info = venue
        if year:
            journal_info += f", {year}"
        if volume:
            journal_info += f", {volume}"
        if issue:
            journal_info += f"({issue})"
        if pages:
            journal_info += f": {pages}"

        # 自动判断期刊等级（简单规则）
        journal_type = self._classify_journal_type(venue, title)

        html = f'''
            <div class="publication-item journal">
                <span class="type">{journal_type}</span>
                <h3>{title}</h3>
                <div class="authors">{authors}</div>
                <div class="venue">{journal_info}</div>
            </div>
        '''

        return html

    def _format_conference_html(self, pub):
        """格式化会议论文HTML"""
        title = pub.get('title', '')
        authors = pub.get('authors', '')
        venue = pub.get('venue', '')
        year = pub.get('year', '')
        pages = pub.get('pages', '')
        citations = pub.get('citations', 0)

        # 生成会议信息
        conference_info = venue
        if year:
            conference_info += f", {year}"
        if pages:
            conference_info += f", pp. {pages}"

        # 自动判断会议等级（简单规则）
        conference_type = self._classify_conference_type(venue, title)

        html = f'''
            <div class="publication-item">
                <span class="type">{conference_type}</span>
                <h3>{title}</h3>
                <div class="authors">{authors}</div>
                <div class="venue">{conference_info}</div>
            </div>
        '''

        return html

    def _classify_journal_type(self, venue, title):
        """自动判断期刊类型"""
        venue_lower = venue.lower()
        title_lower = title.lower()

        # 判断等级（简单规则）
        if 'expert systems with applications' in venue_lower:
            return '中科院 1区 Top'
        elif 'speech communication' in venue_lower:
            return '中科院 2区 · 语音顶级期刊 · CCF-B'
        elif 'neural networks' in venue_lower:
            return '中科院 2区 · CCF-B'
        elif 'signal processing' in venue_lower:
            return '中科院 3区 · CCF-C'
        else:
            return 'SCI期刊'

    def _classify_conference_type(self, venue, title):
        """自动判断会议等级"""
        venue_lower = venue.lower()

        if 'icassp' in venue_lower:
            return 'CCF-B'
        elif 'interspeech' in venue_lower:
            return 'CCF-C'
        elif 'iconip' in venue_lower or 'ijcnn' in venue_lower:
            return 'CCF-C'
        elif 'icml' in venue_lower or 'neurips' in venue_lower:
            return 'CCF-A'
        else:
            return '国际会议'

    def save_json(self, output_file):
        """保存为JSON格式"""
        data = {
            'author_info': self.author_info,
            'publications': self.publications,
            'last_updated': datetime.now().isoformat()
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ JSON数据已保存到: {output_file}")


def main():
    """主函数"""
    print("=" * 60)
    print("Google Scholar Publications Updater")
    print("=" * 60)
    print()

    # 设置作者信息
    AUTHOR_NAME = "Nan Li"
    AFFILIATION = "Tianjin University"

    updater = GoogleScholarUpdater(AUTHOR_NAME, AFFILIATION)

    # 搜索作者
    author = updater.search_author()
    if not author:
        print("❌ 无法找到作者信息")
        sys.exit(1)

    # 获取论文
    publications = updater.fetch_publications(author, max_papers=20)
    if not publications:
        print("❌ 无法获取论文列表")
        sys.exit(1)

    # 生成HTML
    html_content = updater.generate_html('publications.html')

    # 保存JSON
    updater.save_json('publications.json')

    # 显示统计信息
    print()
    print("=" * 60)
    print("📊 统计信息")
    print("=" * 60)
    print(f"总论文数: {len(publications)}")

    journals, conferences = updater.categorize_papers()
    print(f"期刊论文: {len(journals)}")
    print(f"会议论文: {len(conferences)}")
    print()
    print(f"引用总数: {updater.author_info.get('citedby', 0)}")
    print(f"h-index: {updater.author_info.get('hindex', 0)}")
    print(f"i10-index: {updater.author_info.get('i10index', 0)}")
    print()
    print("✅ 更新完成!")
    print()
    print("📄 生成的文件:")
    print("   - publications.html: HTML格式的论文列表")
    print("   - publications.json: JSON格式的原始数据")
    print()
    print("下一步: 将 publications.html 的内容复制到 index.html 和 index-zh.html")


if __name__ == "__main__":
    main()
