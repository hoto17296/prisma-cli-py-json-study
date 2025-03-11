"""フィールドの型を上書きできるか？というアプローチ (できなかった)"""

import asyncio
from typing import TypedDict

from prisma import Prisma
from prisma.bases import BaseChild, BaseParent


class ChildMeta(TypedDict):
    pass


class Child(BaseChild):
    meta: ChildMeta


class ParentMeta(TypedDict):
    pass


class Parent(BaseParent):
    children: list[Child]
    meta: ParentMeta


async def main():
    async with Prisma(auto_register=True):

        # INSERT: ParentCreateInput は書き換えれないのでエラーが出てしまう...
        await Parent.prisma().create(
            {
                "name": "foo",
                "meta": ParentMeta(),
                "children": {
                    "create": [
                        {
                            "name": "bar",
                            "meta": ChildMeta(),
                        }
                    ]
                },
            }
        )

        # SELECT: こちらもエラーが出る
        parent = await Parent.prisma().find_first_or_raise(
            order={"created_at": "desc"},
            include={"children": True},
        )
        print(type(parent.meta))


if __name__ == "__main__":
    asyncio.run(main())
