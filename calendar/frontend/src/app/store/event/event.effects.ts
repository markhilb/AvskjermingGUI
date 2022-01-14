import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { EMPTY } from 'rxjs';
import { catchError, exhaustMap, map } from 'rxjs/operators';
import { EventService } from 'src/app/services/api/event.service';
import * as A from './event.actions';

@Injectable()
export class EventEffects {
  getEvents$ = createEffect(() =>
    this.actions.pipe(
      ofType(A.getEvents),
      exhaustMap(() =>
        this.eventService.getEvents().pipe(
          map((events) => A.getEventsOk({ events })),
          catchError(() => EMPTY),
        ),
      ),
    ),
  );

  createEvent$ = createEffect(() =>
    this.actions.pipe(
      ofType(A.createEvent),
      exhaustMap((action) =>
        this.eventService.createEvent(action.event).pipe(
          map((id) => A.createEventOk({ event: { ...action.event, id } })),
          catchError(() => EMPTY),
        ),
      ),
    ),
  );

  updateEvent$ = createEffect(() =>
    this.actions.pipe(
      ofType(A.updateEvent),
      exhaustMap((action) =>
        this.eventService.updateEvent(action.event).pipe(
          map(() => A.updateEventOk(action)),
          catchError(() => EMPTY),
        ),
      ),
    ),
  );

  deleteEvent$ = createEffect(() =>
    this.actions.pipe(
      ofType(A.deleteEvent),
      exhaustMap((action) =>
        this.eventService.deleteEvent(action.id).pipe(
          map(() => A.deleteEventOk(action)),
          catchError(() => EMPTY),
        ),
      ),
    ),
  );

  constructor(private actions: Actions, private eventService: EventService) {}
}