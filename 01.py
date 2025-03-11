import asyncio
from typing import Any, cast

from prisma import Prisma
from prisma.fields import Json
from prisma.models import Parent


def cast_to_prisma_json(value: Any) -> Json:
    """Prisma の Json 型フィールドの create/update に使用できる値に変換する"""
    return Json(cast(str, value))


async def main():
    async with Prisma(auto_register=True):

        # INSERT: dict を入れることができるが、型を Json にしないといけない
        await Parent.prisma().create(
            {
                "name": "foo",
                "meta": cast_to_prisma_json({}),
                "children": {
                    "create": [
                        {
                            "name": "bar",
                            "meta": cast_to_prisma_json({}),
                        }
                    ]
                },
            }
        )

        # SELECT: 実態は dict だが型ヒントは Json となっているので FastAPI で ResnponseType に指定できない
        parent = await Parent.prisma().find_first_or_raise(
            order={"created_at": "desc"},
            include={"children": True},
        )
        print(type(parent.meta))


if __name__ == "__main__":
    asyncio.run(main())
