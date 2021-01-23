// Code generated by go-swagger; DO NOT EDIT.

package devices

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// NewFindTrafficParams creates a new FindTrafficParams object
// with the default values initialized.
func NewFindTrafficParams() *FindTrafficParams {
	var ()
	return &FindTrafficParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewFindTrafficParamsWithTimeout creates a new FindTrafficParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewFindTrafficParamsWithTimeout(timeout time.Duration) *FindTrafficParams {
	var ()
	return &FindTrafficParams{

		timeout: timeout,
	}
}

// NewFindTrafficParamsWithContext creates a new FindTrafficParams object
// with the default values initialized, and the ability to set a context for a request
func NewFindTrafficParamsWithContext(ctx context.Context) *FindTrafficParams {
	var ()
	return &FindTrafficParams{

		Context: ctx,
	}
}

// NewFindTrafficParamsWithHTTPClient creates a new FindTrafficParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewFindTrafficParamsWithHTTPClient(client *http.Client) *FindTrafficParams {
	var ()
	return &FindTrafficParams{
		HTTPClient: client,
	}
}

/*FindTrafficParams contains all the parameters to send to the API endpoint
for the find traffic operation typically these are written to a http.Request
*/
type FindTrafficParams struct {

	/*Bucket
	  Traffic bucket

	*/
	Bucket *string
	/*Direction
	  Traffic direction

	*/
	Direction string
	/*ID
	  Device UUID

	*/
	ID strfmt.UUID
	/*Interval
	  Traffic interval

	*/
	Interval *string
	/*Timeframe
	  Traffic timeframe

	*/
	Timeframe *types.Timeframe

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the find traffic params
func (o *FindTrafficParams) WithTimeout(timeout time.Duration) *FindTrafficParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the find traffic params
func (o *FindTrafficParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the find traffic params
func (o *FindTrafficParams) WithContext(ctx context.Context) *FindTrafficParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the find traffic params
func (o *FindTrafficParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the find traffic params
func (o *FindTrafficParams) WithHTTPClient(client *http.Client) *FindTrafficParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the find traffic params
func (o *FindTrafficParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithBucket adds the bucket to the find traffic params
func (o *FindTrafficParams) WithBucket(bucket *string) *FindTrafficParams {
	o.SetBucket(bucket)
	return o
}

// SetBucket adds the bucket to the find traffic params
func (o *FindTrafficParams) SetBucket(bucket *string) {
	o.Bucket = bucket
}

// WithDirection adds the direction to the find traffic params
func (o *FindTrafficParams) WithDirection(direction string) *FindTrafficParams {
	o.SetDirection(direction)
	return o
}

// SetDirection adds the direction to the find traffic params
func (o *FindTrafficParams) SetDirection(direction string) {
	o.Direction = direction
}

// WithID adds the id to the find traffic params
func (o *FindTrafficParams) WithID(id strfmt.UUID) *FindTrafficParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the find traffic params
func (o *FindTrafficParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithInterval adds the interval to the find traffic params
func (o *FindTrafficParams) WithInterval(interval *string) *FindTrafficParams {
	o.SetInterval(interval)
	return o
}

// SetInterval adds the interval to the find traffic params
func (o *FindTrafficParams) SetInterval(interval *string) {
	o.Interval = interval
}

// WithTimeframe adds the timeframe to the find traffic params
func (o *FindTrafficParams) WithTimeframe(timeframe *types.Timeframe) *FindTrafficParams {
	o.SetTimeframe(timeframe)
	return o
}

// SetTimeframe adds the timeframe to the find traffic params
func (o *FindTrafficParams) SetTimeframe(timeframe *types.Timeframe) {
	o.Timeframe = timeframe
}

// WriteToRequest writes these params to a swagger request
func (o *FindTrafficParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	if o.Bucket != nil {

		// query param bucket
		var qrBucket string
		if o.Bucket != nil {
			qrBucket = *o.Bucket
		}
		qBucket := qrBucket
		if qBucket != "" {
			if err := r.SetQueryParam("bucket", qBucket); err != nil {
				return err
			}
		}

	}

	// query param direction
	qrDirection := o.Direction
	qDirection := qrDirection
	if qDirection != "" {
		if err := r.SetQueryParam("direction", qDirection); err != nil {
			return err
		}
	}

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if o.Interval != nil {

		// query param interval
		var qrInterval string
		if o.Interval != nil {
			qrInterval = *o.Interval
		}
		qInterval := qrInterval
		if qInterval != "" {
			if err := r.SetQueryParam("interval", qInterval); err != nil {
				return err
			}
		}

	}

	if o.Timeframe != nil {
		if err := r.SetBodyParam(o.Timeframe); err != nil {
			return err
		}
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
