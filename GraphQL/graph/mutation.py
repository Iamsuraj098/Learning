import strawberry
from schema import NoteType, NoteInput
from Service.note import NoteService

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_note(self, input: NoteInput) -> NoteType:
        return await NoteService.create_note(input)
    
    @strawberry.mutation
    async def delete_note(self, note_id: int) -> str:
        return await NoteService.delete(note_id)

    @strawberry.mutation
    async def update_note(self, note_id: int, input: NoteInput) -> str:
        return await NoteService.update(note_id, input)
    